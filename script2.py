# Seem to work a lot faster, but did not really check if it gives rewards
document.querySelectorAll("video").forEach(v => {
  const interval = setInterval(() => {
    v.currentTime += 2;  // Increase by 2 seconds per interval
    if (v.currentTime >= v.duration) {
      clearInterval(interval);
    }
  }, 1);
});
