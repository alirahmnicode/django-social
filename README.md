post app =>

get all posts =>
url : domain/post/

create a post =>
url : domain/post/ (post request)

detail a post => 
url : domain/post/pk/

delete a post =>
url : domain/post/pk/ (delete request)

edit a post => 
url : domain/post/pk/ (put request)

get list of comments => 
url : domain/comments/

create of comments => 
url : domain/comments/ (post request)

delete a comment =>
url : domain/comments/pk/ (delete request)

like and unlike =>
url : domain/post/<int:post_pk>/like-unlike/

search in username =>
url : domain/user/search/q=username (get request)