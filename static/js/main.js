$(document).on("click", "#tweet_btn", function (event) {
    event.preventDefault();
    let $noteForm = $('#tweetForm');
    let $formData = $noteForm.serialize();
    // let $thisURL = $noteForm.attr('data-url') || window.location();

    $.ajax({
        method: 'POST',
        url: '',
        data: $formData,
        success: handleSuccess,
        error: handleError,
    });

    function newTweet($tweet, $likes){
        console.log("New tweet is called");
        return ""+
        "<div class='card'>"+
            "<div class='card-body'>"+
                "<p class='card-text'>"+ $tweet +"</p>"+
                "<button class='like'><i class='fa fa-heart'></i></button>"+
                "<span class='ml-2'>"+ $likes +"</span>"+
            "</div>"+
        "</div>"
    }

    function handleSuccess(data) {

        if (data) {
            // $(".all-tweets").load(" .all-tweets > *");
            $noteForm[0].reset();
        }


        let $tweet = data.tweet;
        let $likes = data.likes;
         $(".all-tweets").prepend(newTweet($tweet, $likes));

        console.log(data.message);
        console.log("Tweet: ",$tweet);
    }

    function handleError(ThrowError) {
        console.log("An error occurred while trying to create the tweet");
        console.log(ThrowError);
    }
});
