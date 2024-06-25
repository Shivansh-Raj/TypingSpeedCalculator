<script>
    // Set the countdown end time (e.g., 5 minutes from now)
    var endTime = new Date().getTime() + 5*60*1000 ;

    function updateTimer() {
        var now = new Date().getTime();
        var distance = endTime - now;

        if (distance >= 0) {
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById("time").innerHTML = minutes + "m " + seconds + "s ";

            setTimeout(updateTimer, 1000);
        } else {
            document.getElementById("time").innerHTML = "Times Up!!";
        }
    }

    updateTimer();
</script>

