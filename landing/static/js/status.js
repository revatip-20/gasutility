document.addEventListener('DOMContentLoaded', function() {
    const statuses = document.querySelectorAll('.status');
    let index = 0;

    function updateStatus() {
        if (index > 0) {
            statuses[index - 1].classList.add('completed');
        }
        if (index < statuses.length) {
            statuses[index].classList.remove('completed'); 
            statuses[index].classList.add('completed');
            index++;
        }
    }

    // Initialize first status as completed
    updateStatus();

    // Update status every 10 seconds
    setInterval(updateStatus, 10000);
});