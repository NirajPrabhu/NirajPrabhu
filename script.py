# Minimal patch for only the navbar/profile popover in user's index.html/style.css/app.js
# We'll extract the first 1000 chars to locate the navigation and insert the minimal changes

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Patch: Add img and popover container after .brand-text with id 'profilePicPopover', and set up id for click
import re
new_nav_brand_part = '''<span class="brand-text" id="brandNameClickable">Niraj Prabhu</span>
<span class="brand-title">Aeronautical Engineer</span>
<!-- Profile Pic Popover -->
<div id="profilePicPopover" class="profile-popover hidden">
    <img src="https://via.placeholder.com/80x80/4A90E2/FFFFFF?text=NP" alt="Niraj Prabhu" class="profile-image" />
</div>'''

html = re.sub(r'<span class="brand-text">Niraj Prabhu<\/span>\s*<span class="brand-title">Aeronautical Engineer<\/span>', new_nav_brand_part, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now add only the minimal CSS for the popover and image
extra_css = '''\n.profile-popover {
  position: absolute;
  left: 0;
  top: 52px;
  background: #fff;
  box-shadow: 0 4px 16px rgba(0,0,0,.17);
  border-radius: 16px;
  padding: 12px 12px 7px 12px;
  z-index: 1002;
  transition: opacity 0.2s;
}
.profile-popover.hidden { display: none; }
.profile-image {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #307ce7;
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(extra_css)

# JavaScript patch: toggle popover on name click, click-out closes, Esc closes
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_patch = '''
// --- Profile Pic Popover Logic ---
document.addEventListener('DOMContentLoaded', function() {
    var brandName = document.getElementById('brandNameClickable');
    var popover = document.getElementById('profilePicPopover');
    if(brandName && popover) {
        brandName.addEventListener('click', function(e) {
            e.stopPropagation();
            popover.classList.toggle('hidden');
        });
        document.addEventListener('click', function(e) {
            if(!popover.contains(e.target) && e.target !== brandName) {
                popover.classList.add('hidden');
            }
        });
        document.addEventListener('keydown', function(e) {
            if(e.key === 'Escape') {
                popover.classList.add('hidden');
            }
        });
    }
});
// --- END Profile Pic Popover Logic ---
'''

# Insert at very end
js += '\n' + js_patch
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

'✔️ Minimal profile picture popover patch applied to index.html, style.css, and app.js.'