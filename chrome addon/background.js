function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

chrome.tabs.onActivated.addListener(function (activeInfo) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {
        id=activeInfo.tabId;

        a = tab.url.includes("polovniautomobili.com");
        b = tab.url.includes("mobile.de");

        if (a == true && b == false){
            chrome.tabs.executeScript(id, 
                {
                    "code": 'document.getElementsByClassName("priceClassified")[0].innerText'
                },
                function(results){
                    price = results;
                    console.log(price);
                    sleep(1000);
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                            console.log(this.responseText);
                        }
                    };
                    xhttp.open("POST", "http://127.0.0.1:5000/send_price");
                    xhttp.send("price=" + price);
                });
                
        } 
        else if (b == true && a == false) {
            chrome.tabs.executeScript(id, 
                {
                    "code": 'document.getElementsByClassName("h3")[1].textContent'
                },
                function(results){
                    price = results;
                    console.log(price);
                    sleep(1000);
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                            console.log(this.responseText);
                        }
                    };
                    xhttp.open("POST", "http://127.0.0.1:5000/send_price");
                    xhttp.send("price=" + price);
                }
            );
            } 
    });
});

chrome.tabs.onActivated.addListener(function (activeInfo) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {
		y = tab.url;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        xhttp.open("POST", "http://127.0.0.1:5000/send_url");
        xhttp.send("url=" + y);
 
    });
});

chrome.tabs.onActivated.addListener(function (activeInfo) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {
		z = tab.title;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        xhttp.open("POST", "http://127.0.0.1:5000/send_title");
        xhttp.send("title=" + z);

    });
});

chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.url) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText); 
            }
        }
        xhttp.open("POST", "http://127.0.0.1:5000/send_url");
        xhttp.send("url=" + change.url);
    }
});

chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.title) {

        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        xhttp.open("POST", "http://127.0.0.1:5000/send_title");
        xhttp.send("title=" + change.title);

    }
});

chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.title) {

        a = tab.url.includes("polovniautomobili.com");
        b = tab.url.includes("mobile.de");

        if (a == true && b == false){
            chrome.tabs.executeScript(tabId, 
                {
                    "code": 'document.getElementsByClassName("priceClassified")[0].innerText'
                },
                function(results){
                    price = results;
                    console.log(price);
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                            console.log(this.responseText);
                        }
                    };
                    xhttp.open("POST", "http://127.0.0.1:5000/send_price");
                    xhttp.send("price=" + price);
                });
                
        } 
        else if (b == true && a == false) {
            chrome.tabs.executeScript(tabId, 
                {
                    "code": 'document.getElementsByClassName("h3")[1].textContent'
                },
                function(results){
                    price = results;
                    console.log(price);
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                            console.log(this.responseText);
                        }
                    };
                    xhttp.open("POST", "http://127.0.0.1:5000/send_price");
                    xhttp.send("price=" + price);
                }
            );
            } 
};
});

var tabToTitle = {};

var tabToUrl = {};

var tabToPrice = {};

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    //store tabId and tab url as key value pair:
    tabToTitle[tabId] = tab.title;
	tabToUrl[tabId] = tab.url;
    tabToPrice[tabId] = tab.price;
});

chrome.tabs.onRemoved.addListener(function (tabId, removeInfo) {
    //since tab is not available inside onRemoved,
    //we have to use the mapping we created above to get the removed tab url:
	console.log(tabToUrl[tabId]);

    var xhttp2 = new XMLHttpRequest();
    xhttp2.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };
    xhttp2.open("POST", "http://127.0.0.1:5000/quit_url");
    xhttp2.send("url=" + tabToUrl[tabId]);

    // Remove information for non-existent tab
	delete tabToUrl[tabId];

});

chrome.tabs.onRemoved.addListener(function (tabId, removeInfo) {
    //since tab is not available inside onRemoved,
    //we have to use the mapping we created above to get the removed tab url:
    console.log(tabToTitle[tabId]);

    var xhttp2 = new XMLHttpRequest();
    xhttp2.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };
    xhttp2.open("POST", "http://127.0.0.1:5000/quit_title");
    xhttp2.send("title=" + tabToTitle[tabId]);

    // Remove information for non-existent tab
    delete tabToTitle[tabId];

});

chrome.tabs.onRemoved.addListener(function (tabId, removeInfo) {
    //since tab is not available inside onRemoved,
    //we have to use the mapping we created above to get the removed tab url:
    console.log(tabToPrice[tabId]);

    var xhttp2 = new XMLHttpRequest();
    xhttp2.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };
    xhttp2.open("POST", "http://127.0.0.1:5000/quit_price");
    xhttp2.send("price=" + tabToPrice[tabId]);

    // Remove information for non-existent tab
    delete tabToPrice[tabId];

});