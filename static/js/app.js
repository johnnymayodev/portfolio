const log = console.log;

log("Hello!");
log("app.js loaded");

const scrollHelperElem = document.querySelector(".scroll-helper");

updateScrollHelper();

setInterval(() => {
  updateScrollHelper();
}, 1000);

function updateScrollHelper() {
  // get user prefer dark mode or light mode
  let prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

  // check if user prefer dark mode
  if (prefersDarkScheme.matches) {
    scrollHelperElem.src =
      "https://img.icons8.com/android/100/f6f6f6/expand-arrow.png";
  } else {
    scrollHelperElem.src =
      "https://img.icons8.com/android/100/323232/expand-arrow.png";
  }
}
