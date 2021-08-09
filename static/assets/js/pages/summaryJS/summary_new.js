function start(){
//    query_cache_by_id
    
    var myURL = head_url+"query_cache_by_id";
    console.log("myURL: "+myURL);
    var summaryId = localStorage.getItem("summaryId");
    var data = {id: summaryId};
//    var address = 'summaryResponse.json';
//    console.log("送出去的data: ");
    console.log(data);
    $.ajax({
        url: myURL,
        data: JSON.stringify(data),
        type: "POST",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log(response);
            summaryContent(response);
        },
        error: function(response){
        }
    });
}

function like(id){
    console.log("按了喜歡");
    var likeNum = document.getElementById(id);
    var number = parseInt(likeNum.innerHTML);
    number += 1;
    likeNum.innerHTML = number;
    console.log("id: "+id);
}

function dislike(id){
    console.log("按了不喜歡");
    var dislikeNum = document.getElementById(id);
    var number = parseInt(dislikeNum.innerHTML);
    number += 1;
    dislikeNum.innerHTML = number;
    console.log("id: "+id);
}

/////////////// 按讚、倒讚 START ///////////////
function objectInArrayThumb(obj, arr){//score, user_id
    for(var i=0; i<arr.length; i++){
        if(obj.score == arr[i].score && obj.user_id == arr[i].user_id){
            return true;
        }
    }
    return false;
}

function thumbs(score, answerId){
    //replyId==""，代表是按貼文的
    // web true代表是網路分數，動態變化的是讚旁邊的數字
    var myURL, data;
    var summaryId = localStorage.getItem("summaryId");
    var userId = localStorage.getItem("sessionID");
    console.log("score: "+score);
    console.log("answerId: "+answerId);
    console.log("summaryId: "+summaryId);
    console.log("userId: "+userId);
    
    var tempId, scoreIcon = '<i class="fa fa-trophy" aria-hidden="true"></i>';
    if(score==1){
        if(answerId==""){// post like
            $("#postScore"+postId).html(scoreIcon + (parseInt($("#postScore"+postId).text())+1));
            tempId = "postLike"+postId;
            document.getElementById(tempId).className = "fa fa-thumbs-up";
            tempId = "postDislike"+postId;
            document.getElementById(tempId).className = "fa fa-thumbs-o-down";
        }
        else{// answer like
            $("#answerScore"+answerId).html(scoreIcon + (parseInt($("#answerScore"+answerId).text())+1));
            tempId = "answerLike"+answerId;
            document.getElementById(tempId).className = "fa fa-thumbs-up";
            tempId = "answerDislike"+answerId;
            document.getElementById(tempId).className = "fa fa-thumbs-o-down";
        }
    }
    else{
        if(answerId==""){//post dislike
            $("#postScore"+postId).html(scoreIcon + (parseInt($("#postScore"+postId).text())-1));
            tempId = "postDislike"+postId;
            document.getElementById(tempId).className = "fa fa-thumbs-down";
            tempId = "postLike"+postId;
            document.getElementById(tempId).className = "fa fa-thumbs-o-up";
        }
        else{// answer dislike
            $("#answerScore"+answerId).html(scoreIcon + (parseInt($("#answerScore"+answerId).text())-1));
            tempId = "answerDislike"+answerId;
            document.getElementById(tempId).className = "fa fa-thumbs-down";
            tempId = "answerLike"+answerId;
            document.getElementById(tempId).className = "fa fa-thumbs-o-up";
        }
    }
    
    if(postType=="faq"){//代表是faq
        data = {faq_id: postId, answer_id: answerId, user: userId};
        console.log("data: ");
        console.log(data);
        if(score == 1){
            myURL = head_url + "like_faq_post";
//            console.log("API為: like_faq_post");
        }
        else{
            myURL = head_url + "dislike_faq_post";
//            console.log("API為: dislike_faq_post");
        }
        console.log("myURL: "+myURL);
        $.ajax({
            url: myURL,
            type: "POST",
            data: JSON.stringify(data),
            async: false,
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){
                console.log(response);
//                window.location.reload();
            },
            error: function(response){
            }
        });
    }
    else if(postType=="innerPost"){//代表是innerPost
        data = {post_id: postId, response_id: answerId, user: userId, target_user: targetUserId};
        console.log(data);
        if(score == 1){
            myURL = head_url + "like_inner_post";
//            console.log("API為: like_inner_post");
        }
        else{
            myURL = head_url + "dislike_inner_post";
//            console.log("API為: dislike_inner_post");
        }
        $.ajax({
            url: myURL,
            type: "POST",
            data: JSON.stringify(data),
            async: false,
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){
//                console.log(response);
//                window.location.reload();
            },
            error: function(response){
            }
        });
    }
}
/////////////// 按讚、倒讚 END ///////////////

function summaryContent(response){
    console.log("summary: ");
    console.log(response);
    // 問題
    var question = document.getElementById("stackoverflowQuestion");
    var likeScore = 0, dislikeScore = 0;
    
    for(var i=0; i<response.question.score.length; i++){
        if(response.question.score[i].user_vote==1){
            likeScore += 1;
        }
        else if(response.question.score[i].user_vote==-1){
            dislikeScore += 1;
        }
    }
    
    var content = "";
    
    ///////////////////////////// 問題 START /////////////////////////////
    content += '<span style="font-size: 25px; font-weight: bold; width: auto; color: #505458;">';
        content += response.question.title;//標題
        content += '<span style="float: right;">';
            content += '<i class="fa fa-trophy" aria-hidden="true" style="font-size: 10px; color: #505458;"></i>';
            content += '<span style="font-size: 10px; color: #505458;">';
                content += response.question.vote;
            content += '</span>';
        content += '</span>';
    content += '</span>';
    
    content += '<br>';
    
    content += '<a href="';
    content += response.link;
    content += '" target="_blank">點我看原文</a>';
    
    content += '<br><br>';
    
    content += '<div style="font-size: 16px; font-weight: bold; width: auto; color: #505458;">摘要: </div>';
    content += '<div style="margin-top: 10px; font-size: 12px;">';
        content += response.question.abstract;
    content += '</div>';

    
    content += '<br><br>';
    
    content += '<div style="font-size: 16px; font-weight: bold; width: auto; color: #505458;">原始內容: </div>';
    content += '<div style="margin-top: 10px; font-size: 12px;">';
        content += response.question.content;
    content += '</div>';

    // 倒讚 START
    content += '<button type="button" class="scoreBtn" style="float: right;"><i class="fa fa-thumbs-o-down" aria-hidden="true"></i>';
    content += '</button>'; 
    // 倒讚 END
    
    // 讚 START
    content += '<button type="button" class="scoreBtn" style="float: right;"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i>';
    content += '</button>';
    // 讚 END
    
    content += '<span class="badge badge-default purpleLabel2" style=" background-color: white;">';
        content += response.time.slice(0, 10);
    content += '</span>';
    question.innerHTML = content;
    hljs.highlightAll();
    ///////////////////////////// 問題 END /////////////////////////////
    
    ///////////////////////////// 回覆 START /////////////////////////////
    var comment = document.getElementById("accordion");
    content = "";
    for(var i=0; i<response.answers.length; i++){
        var likeScore = 0, dislikeScore = 0;
        for(var j=0; j<response.answers[i].score.length; j++){
            if(response.answers[i].user_vote==1){
                likeScore += 1;
            }
            else if(response.answers[i].user_vote==-1){
                dislikeScore += 1;    
            }
        }
        content += '<div class="accordion-panel">';//第一個div
//        //----- 解答的標題 START -----//
            content += '<div class="accordion-heading" role="tab" id="heading';
            content += i;
            content += '">';
            
                content += '<h3 class="card-title accordion-title">';
                    content += '<a class="accordion-msg" data-toggle="collapse" data-parent="#accordion" href="#collapse';
                    content += i;
                    content += '" aria-expanded="true" aria-controls="collapse';
                    content += i;
                    content += '">';
                        content += '最佳解答'
                        content += (i+1);
                    
        
                        content += '<div style="float: right; font-size: 15px;">';

                            content += '<button type="button" class="scoreBtn"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i>';
                            content += '</button>';
        
                            content += '<button type="button" class="scoreBtn" style="margin-right: 10px;"><i class="fa fa-thumbs-o-down" aria-hidden="true"></i>';
                            content += '</button>';
        
                            content += '<i class="fa fa-trophy" aria-hidden="true" style="color: #505458;"></i>';
        
                            content += '<span style="margin-right: 5px; color: #505458;">';
                            content += response.answers[i].vote;
                            content += '</span>';
                    
                        content += '</div>';
                        
                    content += '</a>';
                content += '</h3>';
            content += '</div>';
            //----- 解答的標題 END -----//
        
            //----- 解答 START -----//
            content += '<div id="collapse';
            content += i;
            content += '" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="heading';
            content += i;
            content += '">';

                content += '<div class="accordion-content accordion-desc">';
        
                    content += '<p>';
                        content += '<a href="';
                        content += response.link;
                        content += '#';
                        content += response.answers[i].id;
                        content += '" target="_blank">點我看原文</a><br><br>';
        
                        // 摘要 START
                        content += '<div style="font-size: 16px; font-weight: bold; width: auto; color: #505458;">摘要: </div>';
                        content += '<div style="margin-top: 10px; font-size: 12px;">';
                            content += response.answers[i].abstract;
                        content += '</div>';
                        // 摘要END
                        
                        // 原內容 START
                        content += '<div style="font-size: 16px; font-weight: bold; width: auto; color: #505458;">原始內容: </div>';
                        content += '<div style="margin-top: 10px; font-size: 12px;">';
                            content += response.answers[i].content;
                        content += '</div>';
                        // 原內容END
                        
                    content += '</p>';
                content += '</div>';
            content += '</div>';
            //----- 解答 END -----//
        content += '</div>';
        ///////////////////////////// 回覆 END /////////////////////////////
    }
    comment.innerHTML = content;
}

window.addEventListener("load", start, false);