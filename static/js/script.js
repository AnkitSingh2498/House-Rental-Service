$('.login-form .one input').focus(function(){
  $('.login-form .one label').css('color','#010ac2');
  $('.login-form .two label').css('color','#000');
  $('.login-form .three label').css('color','#000');
});
$('.login-form .two input').focus(function(){
  $('.login-form .one label').css('color','#000');
  $('.login-form .two label').css('color','#010ac2');
  $('.login-form .three label').css('color','#000');
});
$('.login-form .three input').focus(function(){
  $('.login-form .one label').css('color','#000');
  $('.login-form .two label').css('color','#000');
  $('.login-form .three label').css('color','#010ac2');
});


$('.login-box').click(function(e){
  e.preventDefault();
  $('.reg').css('transform','translatex(-700px)');
  $('.reg').css('transition','0.5s');
  $('.reg').css('opacity','0');

});
$('.regbox').click(function(f){
  f.preventDefault();

  $('.reg').css('transform','translatex(0px)');
  $('.reg').css('transition','0.5s');
  $('.reg').css('opacity','1');

});


// $('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
//     var $this = $(this),
//         label = $this.prev('label');
  
//         if (e.type === 'keyup') {
//               if ($this.val() === '') {
//             label.removeClass('active highlight');
//           } else {
//             label.addClass('active highlight');
//           }
//       } else if (e.type === 'blur') {
//           if( $this.val() === '' ) {
//               label.removeClass('active highlight'); 
//               } else {
//               label.removeClass('highlight');   
//               }   
//       } else if (e.type === 'focus') {
        
//         if( $this.val() === '' ) {
//               label.removeClass('highlight'); 
//               } 
//         else if( $this.val() !== '' ) {
//               label.addClass('highlight');
//               }
//       }
  
//   });
  
//   $('.tab a').on('click', function (e) {
    
//     e.preventDefault();
    
//     $(this).parent().addClass('active');
//     $(this).parent().siblings().removeClass('active');
    
//     target = $(this).attr('href');
  
//     $('.tab-content > div').not(target).hide();
    
//     $(target).fadeIn(600);
    
//   });