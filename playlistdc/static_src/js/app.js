import $ from 'jquery'
import 'foundation'
import 'foundation-mediaquery'


// initialize foundation
$(document).foundation()

// example
const dateDisplayEl = document.createElement('div')
dateDisplayEl.innerHTML = new Date()
document.body.appendChild(dateDisplayEl)



// find template and compile it
var results = document.getElementById('results');
    
    var playingCssClass = 'playing';
    var audioObject = null;


results.addEventListener('click', function (e) {
    var target = e.target;
   	console.log(target)

    if (target !== null && target.classList.contains('cover')) {
        if (target.classList.contains(playingCssClass)) {
            audioObject.pause();
        } else {
            if (audioObject) {
                audioObject.pause();
            }
            audioObject = new Audio(target.getAttribute('data-album-url'));
            audioObject.play();
            target.classList.add(playingCssClass);
            audioObject.addEventListener('ended', function () {
              	target.classList.remove(playingCssClass);
            });
            audioObject.addEventListener('pause', function () {
            	target.classList.remove(playingCssClass);
            });
        }
    }
});

