# ELGI VR Tour

> Interactive 3D virtual tour of the ELGI Industrial Plant with immersive 360° panorama views

[![Production Ready](https://img.shields.io/badge/status-production%20ready-brightgreen)]()
[![GitHub Pages](https://img.shields.io/badge/deploy-GitHub%20Pages-blue)]()

## 🌟 Features

- **Interactive 3D Model**: Explore the industrial plant from any angle
- **Location Pins**: Click to discover different areas and buildings
- **Building Navigation**: Enter buildings to explore internal sections
- **360° VR Tours**: Immersive panorama views with navigation
- **Responsive Design**: Works seamlessly on all devices
- **Audio Feedback**: Interactive sound effects
- **Search & Filter**: Find locations quickly

## 🚀 Quick Start

### View Locally

1. Clone or download this repository
2. Open `index.html` in a modern web browser
3. Click "Got It, Let's Start!" to begin the tour

### Deploy to GitHub Pages

1. Push this repository to GitHub
2. Go to **Settings** → **Pages**
3. Select **main** branch and **/ (root)** folder
4. Your site will be live at `https://[username].github.io/[repo-name]/`

📖 **Full deployment instructions**: See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 📁 Project Structure

```
├── index.html          # Main 3D tour interface
├── vr-tour.html       # 360° panorama tour
├── assets/            # Images, logos, and UI assets
├── images/            # Pin textures and banners
├── Audio/             # Sound effects
└── models/            # 3D model files
```

## 🎮 How to Use

### 3D View
- **Rotate**: Click and drag
- **Zoom**: Mouse wheel or pinch
- **Pan**: Right-click and drag
- **Click Pins**: View location information
- **Enter Buildings**: Explore internal sections

### VR Mode
- **Navigate**: Click navigation arrows
- **Double-tap**: Move to where arrow points
- **Warning Points**: Click to view safety information
- **Mini-map**: Track your location

## 🛠️ Technologies

- **Three.js** - 3D graphics and model rendering
- **A-Frame** - WebXR and VR experiences
- **GSAP** - Smooth animations
- **WebXR** - Virtual reality support

## 📋 Requirements

- Modern web browser (Chrome, Firefox, Edge, Safari)
- JavaScript enabled
- WebGL support
- HTTPS for VR mode (automatically provided by GitHub Pages)

## ✅ Production Ready

This application is fully production-ready with:
- ✅ All asset paths corrected for case-sensitive systems
- ✅ Error handling and fallbacks implemented
- ✅ Optimized for GitHub Pages deployment
- ✅ Cross-browser compatibility
- ✅ Mobile responsive design
- ✅ HTTPS-ready CDN dependencies

## 🔧 Troubleshooting GitHub Pages

### Black Screen in VR Tour
**Cause**: Asset loading failure due to incorrect paths  
**Solution**: 
- Verify all image files are in the `assets/` folder
- Check browser console (F12) for 404 errors
- Ensure `.nojekyll` file exists in root directory

### Logo Not Loading
**Cause**: Incorrect path or missing file  
**Solution**:
- Confirm `assets/elgiequip.png` exists
- Check file name matches exactly (case-sensitive)

### Buttons Not Arranged Properly
**Cause**: CSS not loading or viewport issues  
**Solution**:
- Clear browser cache (Ctrl+Shift+R)
- Check responsive design on different screen sizes
- Verify all CSS is inline in HTML files

### 404 Errors for Images
**Cause**: Case sensitivity on GitHub Pages servers  
**Solution**:
- All paths must use lowercase: `assets/img1.jpg` not `Assets/img1.jpg`
- File names must match exactly

## 📝 License

© 2026 ELGI Equipment Limited. All rights reserved.

## 🤝 Contributing

This is a production application for ELGI Equipment Limited.

## 📞 Support

For issues or questions, please check the [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for troubleshooting tips.

---

**Made with ❤️ for ELGI Equipment Limited**
