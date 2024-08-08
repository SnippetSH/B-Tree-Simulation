/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      borderWidth: {
        '1': '1px',
        '1.5': '1.5px',
        '2.5': '2.5px'
      }
    },
  },
  plugins: [require("tailwind-scrollbar-hide")],
}

