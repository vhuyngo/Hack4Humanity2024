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
        //createAnswer(data.)
        
      })
      .catch(error => {
        console.error('Fetch error:', error);
      });
  }
  