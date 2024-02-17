const apiEndpoint = 'https://your-api-endpoint.com/timestamp';

function fetchTimestampInfo() {
    fetch(apiEndpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Process the timestamp data
            console.log("Timestamp data received:", data);
            // Here you might want to send this data to a content script or handle it otherwise
        })
        .catch(error => {
            console.error("Error fetching timestamp information:", error);
        });
}

// Check for new timestamp information every 10 minutes (600000 milliseconds)
const fetchInterval = 600000; // Adjust this value as needed

// Start the interval as soon as the background script loads
setInterval(fetchTimestampInfo, fetchInterval);

// Optionally, you might also want to fetch the timestamp info immediately when the background script starts
fetchTimestampInfo();
