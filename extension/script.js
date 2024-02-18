const apiEndpoint2 = 'http://172.20.209.75:5003/epilepsy_check';
const webEndpoint = 'ws://172.20.209.75:6789/';

const timeStamps = [];

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

/*
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

      var response = document.getElementById("responseText");
      response.textContent = data;       
      // append to array

    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
}
*/

function sendUrlEmbedded(url) {
  var ws = new WebSocket("ws://172.20.209.75:6789");

  console.log(ws);

  ws.onopen = function() {
      // Websocket is connected, send a message
      console.log("Connected to the server");
      ws.send(url);
  };

  ws.onmessage = function(evt) {
      // Receive and log messages from the server
      console.log("Message from server: " + evt.data);
      var nHTML = "";
      timeStamps.push(evt.data);
      timeStamps.forEach(function(item) {
        nHTML += '<li>' + item + '</li>';
      });
    
      document.getElementById("responseText").innerHTML = '<ul>' + nHTML + '</ul>'
    
  };

  // Optional: Handle any errors that occur
  ws.onerror = function(error) {
      console.log("WebSocket error: " + error.message);
  };

}
