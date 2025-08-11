/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        calendas: ["CalendasPlus", "serif"],
      },
      animation: {
        // pulse-smooth now preserves the translate
        "pulse-smooth": "pulseSmooth 2.5s ease-in-out infinite",
        breathe: "breathe 3s ease-in-out infinite", 
      },
      keyframes: {
        pulseSmooth: {
          "0%, 100%": {
            transform: "translate(-50%, -50%) scale(1)",
            opacity: "0.3",
          },
          "50%": {
            transform: "translate(-50%, -50%) scale(1.05)",
            opacity: "0.4",
          },
        },
        breathe: {
          "0%, 100%": {
            transform: "translate(-50%, -50%) scale(1)",
            filter: "drop-shadow(0 0 6px white)",
          },
          "50%": {
            transform: "translate(-50%, -50%) scale(1.05)",
            filter: "drop-shadow(0 0 12px white)",
          },
        },
      },
    },
  },
  plugins: [],
};
