/* ================ Facebook Login ================= */
// 設定 Facebook JavaScript SDK
var auth2;
window.fbAsyncInit = function () {
    FB.init({
      appId: '1018939978932508',
      cookie: true,
      xfbml: true,
      version: 'v11.0'
    });

    FB.AppEvents.logPageView();

};

(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// 檢查Facebook登入狀態
function checkLoginState() {
    // 先清空localStorage
    localStorage.clear();
// 取得登入狀態資訊
    FB.login(function (response) {
        if (response.status === 'connected') {
        console.log(response)
        // 若已登入則利用facebook api取得使用者資料
        FB.api(
          '/me',
          'GET', {
          "fields": "id,name"
          },
          function (response) {
//              console.log("傳到後端的: "+response);
            // 取得使用者資料丟到後端
            $.ajax({
                type: "POST",
                url: head_url + 'facebook_sign_in',
                data: JSON.stringify(response),
                async: false,
                dataType: "json",
                contentType: 'application/json; charset=utf-8',
                success: function (response_data) {
//                    sessionStorage.setItem('user_id', response_data['_id']);
//                    sessionStorage.setItem('role', response_data['role']);
//                    console.log('user_id :' + sessionStorage.getItem('user_id') + ' ,role: ' + sessionStorage.getItem('role') + ' has logged in.')

                    //慈 START
                    localStorage.setItem("sessionID", response_data['_id']);
                    localStorage.setItem("role", "generalUser");
                    
                    window.location.href = 'https://soselab.asuscomm.com:55002/site/PSAbot';
                    //慈 END
                },
                error: function (xhr, status, error) {
                  console.log('get_data: '+ xhr.responseText + status + ',error_msg: ' + error);
                }
            });
          });
      }
    }
//    , { auth_type: 'reauthenticate' }
    );
}

/* ================================================= */

/* ================ Google Sign in ================= */
function onLoadGoogleCallback(){
  gapi.load('auth2', function(){
    gapi.auth2.init({
      client_id: '417777300686-b6isl0oe0orcju7p5u0cpdeo07hja9qs.apps.googleusercontent.com',
      cookiepolicy: 'none',
      scope: 'profile'
    });
    auth2 = gapi.auth2.getAuthInstance();
    attachSignin(document.getElementById('google-login-btn'));
    auth2.currentUser.listen(userChanged);
  });

  function userChanged(googleUser){
    console.log('user changed.')
    if (googleUser) {
      //傳送access token至後端驗證
      $.ajax({
        type: "POST",
        url: head_url + 'google_sign_in',
        data: JSON.stringify({
          'id_token': googleUser.getAuthResponse().id_token
        }),
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function (response_data) {
          sessionStorage.setItem('user_id', response_data['_id']);
          sessionStorage.setItem('role', response_data['role']);
          console.log('user_id :' + sessionStorage.getItem('user_id') + ' ,role: ' + sessionStorage.getItem('role') + ' has logged in.')
        },
        error: function (xhr, status, error) {
          console.log('get_data: '+ xhr.responseText + status + ',error_msg: ' + error);
        }
      });
    }
  }
  function attachSignin(element) {
    console.log(element.id);
    auth2.attachClickHandler(element, {},
      function(googleUser) 
      {
        // 登入成功
        var profile = googleUser.getBasicProfile();
        //傳送access token至後端驗證
        $.ajax({
          type: "POST",
          url: head_url + 'google_sign_in',
          data: JSON.stringify({
            'id_token': googleUser.getAuthResponse().id_token
          }),
          dataType: "json",
          contentType: 'application/json; charset=utf-8',
          success: function (response_data) {
            sessionStorage.setItem('user_id', response_data['_id']);
            sessionStorage.setItem('role', response_data['role']);
            console.log('user_id :' + sessionStorage.getItem('user_id') + ' ,role: ' + sessionStorage.getItem('role') + ' has logged in.')
          },
          error: function (xhr, status, error) {
            console.log('get_data: '+ xhr.responseText + status + ',error_msg: ' + error);
          }
        });
      }, 
      function(error) 
      {
        //登入失敗
        console.log('Sign-in error', error);
      }
    );
  }
}



/* ================================================= */