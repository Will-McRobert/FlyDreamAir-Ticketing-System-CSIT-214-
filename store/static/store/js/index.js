const selectDatesButton = document.getElementById('select-dates-button');
const flightOriginInput = document.getElementById('flight-origin-input');
const flightDestinationInput = document.getElementById('flight-destination-input');
const flightBookingContainer = document.getElementById('flight-booking-container');
const resultsOriginWrapper = document.getElementById('results-origin');
const resultsDestinationWrapper = document.getElementById('results-destination');

selectDatesButton.onsubmit = () => {
    if (flightOriginInput.value === "" && flightDestinationInput.value === "") {
        alert('Please enter the origin and destination airports.');
        return false;
    }
    else if (flightOriginInput.value === "") {
        alert('Please enter the origin airport.');
        return false;
    }
    else if (flightDestinationInput.value === "") {
        alert('Please enter the destination airport.');
        return false;
    }
}


let locations = ['Sydney', 'Sydney Airport', 'Hobart', 'Los Angeles', 'Tokyo', 'Melbourne', 'Munich', 'Gold Coast', 'Gold Coast Airport', 'Paris'].sort();

// Listens for user input in 'fly from input', displays suggestions to user
flightOriginInput.addEventListener('keyup', () => {
    resultsOriginWrapper.style.display = "block";
   let results = [];
   let input = flightOriginInput.value;

   if (input.length) {
       results = locations.filter((item) => {
           return item.toLowerCase().includes(input.toLowerCase());
       });
   }

   renderResults(results, resultsOriginWrapper);
});

flightDestinationInput.addEventListener('keyup', () => {
    resultsDestinationWrapper.style.display = "block";
   let results = [];
   let input = flightDestinationInput.value;

   if (input.length) {
       results = locations.filter((item) => {
           return item.toLowerCase().includes(input.toLowerCase());
       });
   }

   renderResults(results, resultsDestinationWrapper);
});


function renderResults(results, div) {
    if (!results.length) {
        return div.classList.remove('show');
    }

    let content = results.map((item) => {
        return `<li>${item}</li><br>`
    }).join('');

    div.classList.add('show');
    div.innerHTML = `<ul>${content}</ul>`;
}
//
// function displayLocations(value) {
//     flightOriginInput.value = value;
// }

selectDatesButton.onclick = () => {
    location.href = "flight-select";
};

flightOriginInput.addEventListener('focusout', () => {
    resultsOriginWrapper.style.display = "none";
});

flightDestinationInput.addEventListener('focusout', () => {
    resultsDestinationWrapper.style.display = "none";
});