const apiEndpoint2 = 'http://172.20.215.140:5003/epilepsy_check';

chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    // tabs is an array of tab objects
    var currentTab = tabs[0];
    
    // Access the URL of the current tab
    var currentTabUrl = currentTab.url;
    
    // Now you can use currentTabUrl as needed
    document.getElementById("urlInput").value = currentTabUrl;
  
  
});
  
document.getElementById("openButton").addEventListener("click", function() {
    openUrl();
});
  

function openUrl() {
    var url = document.getElementById("urlInput").value;
    if (url) {
        sendUrlEmbedded(url);  // api call to send url
        saveUrl(url);
    }
}

// test if url is saved
function saveUrl(url) {
    console.log("URL saved:", url);
}

// send embedded url
function sendUrlEmbedded(url) {
    const fullApiUrl = `${apiEndpoint2}`;
    const headers = {
      'Content-Type': 'application/json',
    };
    const requestBody = JSON.stringify({ url: url });
    fetch(fullApiUrl, {
      method: 'POST',
      headers: headers,
      body: requestBody,
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log("sucess for 2", data);
        chrome.storage.local.set({timestampData: data}, function() {
          console.log('Timestamp information is saved.');
        });
        //createAnswer(data.)        
      })
      .catch(error => {
        console.error('Fetch error:', error);
      });
  }
  
document.addEventListener('DOMContentLoaded', function() {
  chrome.storage.local.get(['timestampData'], function(result) {
      if (result.timestampData) {
          // Display the timestamp information to the user
          console.log('Timestamp data:', result.timestampData);
          // For example, update DOM elements here

          // Optionally clear the stored data if you don't need it anymore
          chrome.storage.local.remove(['timestampData'], function() {
              console.log('Timestamp information was retrieved and cleared.');
          });
      }
  });
});
