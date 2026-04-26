/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // enables manual toggling
  content: [
    "./index.html",   // include your HTML file
    "./style.css"     // include your CSS if you use @tailwind directives
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
