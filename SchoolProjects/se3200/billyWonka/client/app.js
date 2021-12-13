console.log("App Loaded")

loadTicketsFromServer()

var dayOfTheWeek = new Date().getDay();

var applicantName = document.querySelector("#applicantName")
var applicantAge = document.querySelector("#applicantAge")
var applicantGuest = document.querySelector("#applicantGuest")
var submitButton = document.querySelector("#submit")

var ticketsDiv = document.querySelector("#tickets")

console.log(applicantName, applicantAge, applicantGuest, submitButton, ticketsDiv)

submitButton.onclick = function(){
    var appName = applicantName.value;
    var appAge = applicantAge.value;
    var appGuest = applicantGuest.value;

    createTicket(appName, appAge, appGuest);

    applicantName.value = "";
    applicantAge.value = "";
    applicantGuest.value = "";
}

function loadTicketsFromServer(){ 

    fetch("http://localhost:8080/tickets",{
    //credentials: 'include',
    
    }).then(function(response) {

        response.json().then(function (data){

            console.log("tickets from server ", data);
            displayTickets(data)
        }); 
    });
}

function displayTickets(data){
    ticketsDiv.innerHTML = "";
    var hrLine = document.createElement("hr")
    ticketsDiv.appendChild(hrLine)
    
    data.forEach(function(ticket){
        var newTicket = document.createElement("li");
        var innerDiv = document.createElement("div");

        var entrantName = document.createElement("div");
        entrantName.innerHTML = "Applicant's Name: " + ticket.entrant_name;
        innerDiv.appendChild(entrantName);     

        newTicket.appendChild(innerDiv);

        var entrantAge = document.createElement("div");
        entrantAge.innerHTML = "Applicant's Age: " + ticket.entrant_age;
        innerDiv.appendChild(entrantAge);

        newTicket.appendChild(innerDiv);

        var entrantGuest = document.createElement("div");
        entrantGuest.innerHTML = "Applicant's Guest: " + ticket.guest_name;
        innerDiv.appendChild(entrantGuest);

        console.log("day of the week ", dayOfTheWeek)
        
        if(ticket.random_token == dayOfTheWeek){
            newTicket.classList.add("golden");
        }
        else{
            newTicket.classList.add("normal");
        }

        newTicket.appendChild(innerDiv);
        ticketsDiv.appendChild(newTicket);

    })
}

function createTicket(applicantName, applicantAge, applicantGuest){
    var ticketData = (
        "entrant_name=" + encodeURIComponent(applicantName)
        + "&entrant_age=" + encodeURIComponent(applicantAge)
        + "&guest_name=" + encodeURIComponent(applicantGuest)
    );
    console.log(ticketData)
    

    fetch("http://localhost:8080/tickets", { 
        method: "POST",
        body: ticketData,
        credentials: 'include',
        headers: {"Content-Type": "application/x-www-form-urlencoded"}

     }).then(function(response){
        if (response.status == 403) {
            response.text().then(function (text) {
                alert(text);
                console.log("text?", text);
            });
          }
          else if (response.status == 201) {
                alert("Submission recieved");
            };
            
         loadTicketsFromServer();
        })
}