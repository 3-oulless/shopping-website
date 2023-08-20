function send_comment(){
    document.getElementById('comment').scrollIntoView({behavior:"smooth"});
}

function answers(parentId){
    document.getElementById('parent_id').value = parentId
    document.getElementById('answer_comment').scrollIntoView({behavior:"smooth"});

}

function shoLargeImage(imageSrc){
    console.log(imageSrc)
    main_image = document.getElementById('main_image')
    main_image.attr('src',imageSrc)
}