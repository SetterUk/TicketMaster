// Seat selection functionality for the booking page

document.addEventListener('DOMContentLoaded', function() {
    // Make sure this script only runs on the booking page
    if (!document.querySelector('.seat-map')) {
        return;
    }
    
    // Additional seat selection related functionality could be added here
    // Most of the seat selection logic is already implemented inline in the template
    
    // Handle form submission
    const bookingForm = document.getElementById('booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            const selectedSeats = document.querySelectorAll('input[name="seats"]');
            if (selectedSeats.length === 0) {
                e.preventDefault();
                alert('Please select at least one seat before booking.');
            }
        });
    }
});
