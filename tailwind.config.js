/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#020617",
        primary: {
          DEFAULT: "#00d4ff",
          dark: "#0099ff",
          glow: "rgba(0, 212, 255, 0.3)",
        },
        accent: {
          DEFAULT: "#7000ff",
          glow: "rgba(112, 0, 255, 0.3)",
        },
        danger: {
          DEFAULT: "#ff0055",
          glow: "rgba(255, 0, 85, 0.3)",
        },
        success: "#00ff99",
        text: {
          main: "#f8fafc",
          muted: "#94a3b8",
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      backgroundImage: {
        'grid-pattern': "url('data:image/svg+xml,%3Csvg width=\"40\" height=\"40\" viewBox=\"0 0 40 40\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cpath d=\"M0 0h40v40H0V0zm1 1h38v38H1V1z\" fill=\"rgba(0, 212, 255, 0.05)\" fill-rule=\"evenodd\"/%3E%3C/svg%3E')",
      },
      animation: {
        'pulse-glow': 'pulse-glow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        'pulse-glow': {
          '0%, 100%': { opacity: 1 },
          '50%': { opacity: .5 },
        }
      }
    },
  },
  plugins: [],
}
