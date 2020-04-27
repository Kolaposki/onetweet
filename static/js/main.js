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

    function handleSuccess(data) {

        if (data) {
            $(".all-tweets").load(" .all-tweets > *");
            $noteForm[0].reset();
        }

        console.log("Tweet: ",data.tweet);
        console.log("Content: ",data.content);
        console.log("Pk: ",data.pk);
    }

    function handleError(ThrowError) {
        console.log("An error occurred while trying to create the note");
        console.log(ThrowError);
    }
});
