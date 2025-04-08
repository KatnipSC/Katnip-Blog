document.addEventListener('DOMContentLoaded', () => {
  const theme_toggle = document.getElementById("theme-toggle");
  const dark_to_light = "🌒 🌓 🌔 🌕".split(" ");
  const light_to_dark = "🌖 🌗 🌘 🌑".split(" ");
  var theme = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

  theme_toggle.innerHTML = theme ? "🌕" : "🌑";

  theme_toggle.addEventListener("click", () => {
    console.log("Theme toggled");
    theme = !theme;
    const transition = theme ? dark_to_light : light_to_dark;
  document.documentElement.style.setProperty("color-scheme", theme ? "dark" : "light");
    for (let i=0;i<4;i++){
      setTimeout(() => {
        theme_toggle.innerHTML = transition[i];
      }, i * 100);
    }
  })
});
                        