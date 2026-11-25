```html
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AURA // ATELIER — AI Personal Styling & Virtual Try-On</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Google Fonts: Cormorant Garamond (Editorial Serif) & Plus Jakarta Sans (Clean Modern UI) & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=JetBrains+Mono:wght@400;500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- MediaPipe FaceMesh (Optional Live ML Enhancement with Seamless Algorithmic Fallback) -->
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh.js" crossorigin="anonymous"></script>

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            obsidian: {
              950: '#070709',
              900: '#0D0E12',
              850: '#13151B',
              800: '#1A1D24',
              700: '#262A34',
            },
            champagne: {
              100: '#FAF5EB',
              200: '#F2E5CE',
              300: '#E5CFA8',
              400: '#D4B47C',
              500: '#C29B57',
              600: '#9E7B3E',
            }
          },
          animation: {
            'scan-beam': 'scanBeam 2.4s ease-in-out infinite',
            'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
          },
          keyframes: {
            scanBeam: {
              '0%, 100%': { top: '8%', opacity: '0.2' },
              '50%': { top: '90%', opacity: '0.95' },
            }
          }
        }
      }
    }
  </script>

  <style>
    /* Custom editorial scrollbar and subtle glassmorphism utilities */
    body {
      background-color: #070709;
      color: #F4F3EF;
      overflow-x: hidden;
    }

    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0D0E12;
    }
    ::-webkit-scrollbar-thumb {
      background: #262A34;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #D4B47C;
    }

    /* Range Slider Styling */
    input[type="range"] {
      -webkit-appearance: none;
      appearance: none;
      background: transparent;
      cursor: pointer;
    }
    input[type="range"]::-webkit-slider-runnable-track {
      height: 4px;
      border-radius: 999px;
      background: #262A34;
    }
    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #D4B47C;
      margin-top: -5px;
      box-shadow: 0 0 10px rgba(212, 180, 124, 0.5);
      transition: transform 0.15s ease;
    }
    input[type="range"]::-webkit-slider-thumb:hover {
      transform: scale(1.2);
    }

    .glass-panel {
      background: rgba(19, 21, 27, 0.78);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.07);
    }

    .gold-gradient-text {
      background: linear-gradient(135deg, #F2E5CE 0%, #D4B47C 50%, #A98344 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .canvas-checkerboard {
      background-image: radial-gradient(#262A34 1px, transparent 1px);
      background-size: 20px 20px;
    }
  </style>
</head>
<body class="font-sans antialiased selection:bg-champagne-400/30 selection:text-champagne-200 min-h-screen flex flex-col">

  <!-- Toast Notification Banner (Replaces alert()) -->
  <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

  <!-- Top Editorial Header -->
  <header class="sticky top-0 z-40 glass-panel border-b border-white/5 px-4 sm:px-8 py-3.5">
    <div class="max-w-[1440px] mx-auto flex flex-wrap items-center justify-between gap-4">
      <!-- Brand Identity -->
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-champagne-300 to-champagne-600 flex items-center justify-center text-obsidian-950 font-serif font-bold text-xl shadow-lg shadow-champagne-500/20">
          A
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="font-serif text-xl sm:text-2xl tracking-wider font-semibold text-white">AURA <span class="text-champagne-400 font-normal">//</span> ATELIER</span>
            <span class="hidden sm:inline-block text-[10px] font-mono uppercase tracking-widest px-2 py-0.5 rounded-full bg-champagne-400/10 text-champagne-300 border border-champagne-400/20">Biometric Stylist v2.6</span>
          </div>
          <p class="text-[11px] text-zinc-400 tracking-wide hidden md:block">Facial Architecture & Bespoke Virtual Try-On Studio</p>
        </div>
      </div>

      <!-- Primary Input & Mode Controls -->
      <div class="flex items-center gap-2 sm:gap-3">
        <button id="btn-webcam" onclick="toggleWebcam()" class="flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-medium bg-obsidian-800 hover:bg-obsidian-700 text-zinc-200 border border-white/10 transition-all">
          <i data-lucide="camera" class="w-4 h-4 text-champagne-400"></i>
          <span id="webcam-btn-label">Live Scan</span>
        </button>

        <label class="flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-medium bg-obsidian-800 hover:bg-obsidian-700 text-zinc-200 border border-white/10 cursor-pointer transition-all">
          <i data-lucide="upload" class="w-4 h-4 text-champagne-400"></i>
          <span>Upload Photo</span>
          <input type="file" id="photo-upload" accept="image/*" class="hidden" onchange="handleImageUpload(event)" />
        </label>

        <button onclick="cyclePresetPortrait()" class="hidden sm:flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-medium bg-obsidian-800 hover:bg-obsidian-700 text-zinc-300 border border-white/10 transition-all" title="Load Editorial Studio Model">
          <i data-lucide="sparkles" class="w-3.5 h-3.5 text-champagne-400"></i>
          <span>Studio Model</span>
        </button>

        <button id="btn-rescan" onclick="triggerBiometricScan()" class="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-gradient-to-r from-champagne-400 to-champagne-500 hover:from-champagne-300 hover:to-champagne-400 text-obsidian-950 shadow-lg shadow-champagne-500/20 transition-all">
          <i data-lucide="scan-face" class="w-4 h-4"></i>
          <span>Analyze Face</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Main Workspace -->
  <main class="flex-1 max-w-[1440px] w-full mx-auto px-4 sm:px-8 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
    
    <!-- LEFT / CENTER COLUMN: Interactive Biometric Canvas & Virtual Try-On Studio (7 cols on lg) -->
    <section class="lg:col-span-7 flex flex-col gap-5">
      
      <!-- Canvas Toolbar -->
      <div class="glass-panel rounded-2xl p-3 flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-1.5 bg-obsidian-950/80 p-1 rounded-xl border border-white/5">
          <button id="mode-tryon" onclick="setCanvasMode('tryon')" class="px-3 py-1.5 rounded-lg text-xs font-medium bg-champagne-400 text-obsidian-950 transition-all flex items-center gap-1.5">
            <i data-lucide="layers" class="w-3.5 h-3.5"></i>
            Virtual Try-On
          </button>
          <button id="mode-compare" onclick="setCanvasMode('compare')" class="px-3 py-1.5 rounded-lg text-xs font-medium text-zinc-400 hover:text-white transition-all flex items-center gap-1.5">
            <i data-lucide="split-square-horizontal" class="w-3.5 h-3.5"></i>
            Before / After
          </button>
          <button id="mode-landmarks" onclick="setCanvasMode('landmarks')" class="px-3 py-1.5 rounded-lg text-xs font-medium text-zinc-400 hover:text-white transition-all flex items-center gap-1.5">
            <i data-lucide="crosshair" class="w-3.5 h-3.5"></i>
            Tune Landmarks
          </button>
        </div>

        <div class="flex items-center gap-2">
          <button id="toggle-mesh-btn" onclick="toggleMeshOverlay()" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-obsidian-800 text-champagne-300 border border-champagne-400/30 hover:bg-obsidian-700 transition-all flex items-center gap-1.5">
            <i data-lucide="scan" class="w-3.5 h-3.5"></i>
            <span>Mesh: ON</span>
          </button>
          <button onclick="exportLookSnapshot()" class="px-3 py-1.5 rounded-xl text-xs font-medium bg-obsidian-800 text-zinc-200 border border-white/10 hover:bg-obsidian-700 transition-all flex items-center gap-1.5" title="Download Styled Portrait">
            <i data-lucide="download" class="w-3.5 h-3.5 text-champagne-400"></i>
            <span class="hidden sm:inline">Save Look</span>
          </button>
        </div>
      </div>

      <!-- Main Viewport Frame -->
      <div id="viewport-wrapper" class="relative w-full aspect-[4/5] sm:aspect-[16/15] max-h-[680px] rounded-3xl overflow-hidden glass-panel canvas-checkerboard border border-white/10 shadow-2xl select-none">
        
        <!-- Hidden Video Element for Webcam Feed -->
        <video id="webcam-video" autoplay playsinline muted class="hidden"></video>

        <!-- Primary Interactive Render Canvas -->
        <canvas id="studio-canvas" class="w-full h-full block cursor-grab active:cursor-grabbing"></canvas>

        <!-- Animated Laser Scan Overlay (Shown during scan) -->
        <div id="scan-overlay" class="hidden absolute inset-0 pointer-events-none z-20">
          <div class="absolute inset-0 bg-champagne-400/5"></div>
          <div class="absolute left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-champagne-300 to-transparent shadow-[0_0_20px_#D4B47C] animate-scan-beam"></div>
          <div class="absolute top-4 left-4 bg-obsidian-950/85 border border-champagne-400/40 px-3 py-1.5 rounded-full flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-champagne-400 animate-ping"></span>
            <span class="text-[11px] font-mono text-champagne-200 tracking-wider uppercase" id="scan-status-text">Mapping 68 Facial Landmarks...</span>
          </div>
        </div>

        <!-- Webcam Capture Trigger Overlay -->
        <div id="webcam-controls" class="hidden absolute bottom-5 left-1/2 -translate-x-1/2 z-30 flex items-center gap-3 bg-obsidian-950/90 backdrop-blur-md px-4 py-2.5 rounded-2xl border border-white/15 shadow-2xl">
          <button onclick="captureWebcamFrame()" class="px-5 py-2 rounded-xl bg-champagne-400 hover:bg-champagne-300 text-obsidian-950 font-semibold text-xs flex items-center gap-2 transition-all">
            <i data-lucide="aperture" class="w-4 h-4"></i>
            Capture & Analyze
          </button>
          <button onclick="stopWebcam()" class="px-3 py-2 rounded-xl bg-obsidian-800 hover:bg-obsidian-700 text-zinc-300 text-xs">
            Cancel
          </button>
        </div>

        <!-- Before / After Slider Handle Overlay -->
        <div id="compare-slider-ui" class="hidden absolute inset-y-0 z-20 pointer-events-none" style="left: 50%;">
          <div class="w-0.5 h-full bg-champagne-300 shadow-[0_0_12px_rgba(212,180,124,0.8)]"></div>
          <div class="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-9 h-9 rounded-full bg-obsidian-950 border-2 border-champagne-300 flex items-center justify-center shadow-xl text-champagne-300">
            <i data-lucide="chevrons-left-right" class="w-4 h-4"></i>
          </div>
          <span class="absolute top-4 right-3 px-2.5 py-1 rounded-md bg-obsidian-950/80 text-[10px] font-mono uppercase tracking-wider text-zinc-300 border border-white/10">Original</span>
          <span class="absolute top-4 left-3 px-2.5 py-1 rounded-md bg-champagne-400/90 text-[10px] font-mono uppercase tracking-wider text-obsidian-950 font-semibold">Styled</span>
        </div>

        <!-- Contextual Canvas Helper Pill -->
        <div id="canvas-hint-pill" class="absolute bottom-3 left-3 z-10 px-3 py-1.5 rounded-xl bg-obsidian-950/80 backdrop-blur-md border border-white/10 text-[11px] text-zinc-300 flex items-center gap-2">
          <i data-lucide="move" class="w-3.5 h-3.5 text-champagne-400"></i>
          <span id="canvas-hint-text">Drag hair, beard, or collar directly on canvas to fine-tune fit</span>
        </div>
      </div>

      <!-- Fine-Tune Overlay Adjustments Dock -->
      <div class="glass-panel rounded-2xl p-4">
        <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
          <div class="flex items-center gap-2">
            <span class="text-xs font-semibold uppercase tracking-wider text-champagne-300">Active Layer Controls</span>
            <div class="flex items-center gap-1 bg-obsidian-950 p-1 rounded-lg border border-white/5">
              <button onclick="selectActiveLayer('hair')" id="layer-tab-hair" class="px-2.5 py-1 rounded-md text-[11px] font-medium bg-obsidian-800 text-champagne-300 border border-champagne-400/30">Hairstyle</button>
              <button onclick="selectActiveLayer('beard')" id="layer-tab-beard" class="px-2.5 py-1 rounded-md text-[11px] font-medium text-zinc-400 hover:text-white">Beard / Grooming</button>
              <button onclick="selectActiveLayer('outfit')" id="layer-tab-outfit" class="px-2.5 py-1 rounded-md text-[11px] font-medium text-zinc-400 hover:text-white">Outfit Collar</button>
            </div>
          </div>

          <button onclick="resetActiveLayerTransform()" class="text-[11px] text-zinc-400 hover:text-champagne-300 flex items-center gap-1 transition-colors">
            <i data-lucide="rotate-ccw" class="w-3 h-3"></i>
            Auto-Align to Landmarks
          </button>
        </div>

        <!-- Sliders Grid -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-1">
          <div>
            <div class="flex justify-between text-[11px] text-zinc-400 mb-1">
              <span>Scale</span>
              <span id="val-scale" class="font-mono text-zinc-200">100%</span>
            </div>
            <input type="range" id="ctrl-scale" min="60" max="150" value="100" oninput="updateLayerControl('scale', this.value)" class="w-full" />
          </div>
          <div>
            <div class="flex justify-between text-[11px] text-zinc-400 mb-1">
              <span>Vertical Offset</span>
              <span id="val-offsetY" class="font-mono text-zinc-200">0px</span>
            </div>
            <input type="range" id="ctrl-offsetY" min="-120" max="120" value="0" oninput="updateLayerControl('offsetY', this.value)" class="w-full" />
          </div>
          <div>
            <div class="flex justify-between text-[11px] text-zinc-400 mb-1">
              <span>Opacity / Blend</span>
              <span id="val-opacity" class="font-mono text-zinc-200">92%</span>
            </div>
            <input type="range" id="ctrl-opacity" min="20" max="100" value="92" oninput="updateLayerControl('opacity', this.value)" class="w-full" />
          </div>
          <div>
            <div class="flex justify-between text-[11px] text-zinc-400 mb-1">
              <span>Tone / Shade</span>
              <span id="val-color-name" class="font-mono text-champagne-300">Espresso</span>
            </div>
            <div id="layer-color-swatches" class="flex items-center gap-1.5 pt-0.5">
              <!-- Populated dynamically per layer -->
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- RIGHT COLUMN: Biometric Diagnostics, Tailored Recommendations & Summary Card (5 cols on lg) -->
    <aside class="lg:col-span-5 flex flex-col gap-5">
      
      <!-- 1. Biometric Style Profile Card -->
      <div class="glass-panel rounded-3xl p-5 border border-champagne-400/20 relative overflow-hidden">
        <div class="absolute -top-16 -right-16 w-40 h-40 rounded-full bg-champagne-400/10 blur-3xl pointer-events-none"></div>
        
        <div class="flex items-start justify-between gap-3 mb-4">
          <div>
            <span class="text-[10px] font-mono uppercase tracking-widest text-champagne-400">Biometric Dossier</span>
            <h2 class="font-serif text-2xl font-semibold text-white mt-0.5">Facial Architecture Profile</h2>
          </div>
          <div class="text-right">
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-[11px] font-mono">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span id="confidence-badge">98.4% Match</span>
            </span>
          </div>
        </div>

        <!-- 3 Core Metrics Grid -->
        <div class="grid grid-cols-3 gap-2.5 mb-4">
          <!-- Face Shape -->
          <div class="bg-obsidian-950/80 rounded-2xl p-3 border border-white/5">
            <span class="text-[10px] uppercase tracking-wider text-zinc-400 block">Face Shape</span>
            <span id="metric-faceshape" class="font-serif text-xl font-semibold text-champagne-200 capitalize block mt-0.5">Oval</span>
            <span id="metric-ratio" class="text-[10px] font-mono text-zinc-500 block mt-0.5">L:W 1.38</span>
          </div>

          <!-- Skin Tone & Undertone -->
          <div class="bg-obsidian-950/80 rounded-2xl p-3 border border-white/5">
            <span class="text-[10px] uppercase tracking-wider text-zinc-400 block">Skin & Tone</span>
            <div class="flex items-center gap-1.5 mt-1">
              <span id="metric-skin-swatch" class="w-4 h-4 rounded-full border border-white/30 shrink-0" style="background-color: #D9A78B;"></span>
              <span id="metric-skintone" class="font-serif text-lg font-semibold text-white leading-tight truncate">Medium</span>
            </div>
            <span id="metric-undertone" class="text-[10px] font-mono text-champagne-300 block mt-0.5">Warm Golden</span>
          </div>

          <!-- Jawline Structure -->
          <div class="bg-obsidian-950/80 rounded-2xl p-3 border border-white/5">
            <span class="text-[10px] uppercase tracking-wider text-zinc-400 block">Jawline</span>
            <span id="metric-jawline" class="font-serif text-xl font-semibold text-white block mt-0.5">Balanced</span>
            <span id="metric-jawangle" class="text-[10px] font-mono text-zinc-500 block mt-0.5">124° Gonial</span>
          </div>
        </div>

        <!-- Manual Override Pills (Allows user to test different detected shapes anytime) -->
        <div class="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-white/5">
          <span class="text-[11px] text-zinc-400">Calibrate Shape:</span>
          <div class="flex flex-wrap gap-1">
            <button onclick="overrideFaceShape('oval')" class="shape-pill px-2 py-0.5 rounded-md text-[11px] bg-champagne-400/20 text-champagne-200 border border-champagne-400/40" data-shape="oval">Oval</button>
            <button onclick="overrideFaceShape('round')" class="shape-pill px-2 py-0.5 rounded-md text-[11px] bg-obsidian-800 text-zinc-400 hover:text-white" data-shape="round">Round</button>
            <button onclick="overrideFaceShape('square')" class="shape-pill px-2 py-0.5 rounded-md text-[11px] bg-obsidian-800 tex