/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("Sidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("Sidenav").style.width = "0";
}

function makeid() {
    return Math.floor(Math.random() * 20)
}



function validate() {

        var temp_array = [];


        if (document.getElementById('lower').checked) {
            temp_array.push('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
        }

        if (document.getElementById('upper').checked) {
            temp_array.push('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z');
        }

        if (document.getElementById('numbers').checked) {
            temp_array.push('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
        }

        if (document.getElementById('symbols').checked) {
            temp_array.push('!', '?', '£', '$', '%', '^', '&', '*', '-', '+','@','#');
        }


        function password_creation(){


            var password_array  = [];

            var uppercase_count = 0;
            var i = 0

            for (i; i < document.getElementById('length_password').value; i++) {

                var temp_char = temp_array[Math.floor(Math.random() * temp_array.length)];
                if (temp_char === temp_char.toUpperCase() && temp_char !== temp_char.toLowerCase()){
                    uppercase_count += 1;
                }

                password_array +=  temp_char;
            }


                return password_array;

        }


        document.getElementById("password_result").innerHTML = password_creation();
}
