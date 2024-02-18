const apiEndpoint2 = 'http://172.20.209.75:5003/epilepsy_check';
const webEndpoint = 'ws://172.20.215.140:6789/';

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
  var ws = new WebSocket("ws://172.20.215.140:6789/");

  console.log(ws);

  ws.onopen = function() {
      // Websocket is connected, send a message
      console.log("Connected to the server");
      ws.send(url);
  };

  ws.onmessage = function(evt) {
      timeStamps.length = 0;

      // Receive and log messages from the server
      console.log("Message from server: " + evt.data);

      const arrayOfArrays = JSON.parse(evt.data);

      console.log(arrayOfArrays);
            
      for (i = 0; i < arrayOfArrays.length ; i++) {
        if (arrayOfArrays[i][0] == arrayOfArrays[i][1]) {
          timeStamps.push(arrayOfArrays[i][0]);
          continue;
        }
        timeStamps.push(arrayOfArrays[i]);
      }

      var nHTML = "";
      //timeStamps.push(evt.data);
      //timeStamps.forEach(function(item) {
      // nHTML += '<li>' + item + '</li>';
      //});

      timeStamps.forEach(function(item) {
        nHTML += '[' + item + '] ';
       });

    /*

    for each element in evt.data:
      if element[0] == element[1]:
        print(element[1]\n)
      else:
        print(element[0], element[1]\n)

    */


      //document.getElementById("responseText").innerHTML = evt.data;

      document.getElementById("responseText").innerHTML = '<ul>' + nHTML + '</ul>'
    
  };

  // Optional: Handle any errors that occur
  ws.onerror = function(error) {
      console.log("WebSocket error: " + error.message);
  };

}


/*
L = [];
curr = [x, x];

for i in L[::-1]:
  if i[1] + 1 > curr[1]:
      curr[0] = L[i]
      del i
  else:
      break;

L.append(curr)
*/