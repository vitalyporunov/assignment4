document.addEventListener("DOMContentLoaded", function () {
    
    // Smooth scrolling for all anchor links
    const smoothScroll = (target, duration) => {
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        let startTime = null;

        const ease = (t, b, c, d) => {
            t /= d / 2;
            if (t < 1) return (c / 2) * t * t + b;
            t--;
            return (-c / 2) * (t * (t - 2) - 1) + b;
        };

        const animateScroll = (currentTime) => {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = ease(timeElapsed, startPosition, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animateScroll);
        };

        requestAnimationFrame(animateScroll);
    };

    const scrollLinks = document.querySelectorAll('a[href^="#"]');
    scrollLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                smoothScroll(targetElement, 800);
            }
        });
    });

    // Admin Dashboard: Show and hide different sections based on the clicked button
    function showSection(sectionId) {
        const sections = document.querySelectorAll('.dashboard-section');
        sections.forEach(section => section.style.display = 'none');
        document.getElementById(sectionId).style.display = 'block';
    }

    // Event listeners for dashboard navigation buttons
    const navButtons = document.querySelectorAll(".dashboard-nav .btn");
    navButtons.forEach(button => {
        button.addEventListener("click", function () {
            const sectionId = this.getAttribute("data-section");
            showSection(sectionId);
        });
    });

    // Toggle visibility of sections on page load (defaults to Manage Pets)
    showSection("managePets");

    // Confirm deletion for admin actions
    const deleteButtons = document.querySelectorAll(".btn-danger");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function (e) {
            if (!confirm("Are you sure you want to delete this item?")) {
                e.preventDefault();
            }
        });
    });

    // Optional: Add further interactivity or UI improvements here, if needed
});
