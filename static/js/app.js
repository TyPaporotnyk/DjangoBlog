$(document).ready(() => {
    /* Hamburger menu */
    $(".hamburger").on("click", (e) => {
        $(".hamburger").toggleClass("active");
        $(".header__nav").toggleClass("active");
    })

    /* Load more button */
    $("#load-more").on("click", (e) => {
        console.log("Load more");
    })
});

