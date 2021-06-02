fuctiong down() {
    if (document.documentElement.scrollTop < document.documentElement.scrollHeight) {
        document.documentElement.scrollTop += 1;
    }
}

fuction scrollDown() {
    bottom = setInterval(() => down(), 25);
}

document.addEventListener('wheel',() => clearInterval(bottom));
document.addEventLisnter('click', () => scrollDown());
