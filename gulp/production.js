import fs from 'fs'
import gulp from 'gulp'
import cleancss from 'gulp-clean-css'
import uglify from 'gulp-uglify'
import header from 'gulp-header'


gulp.task('minify:css', () =>
  gulp.src('./playlistdc/static/**/*.css')
    .pipe(cleancss())
    .pipe(gulp.dest('./playlistdc/static/')))

gulp.task('minify:js', () =>
  gulp.src('./playlistdc/static/**/*.js')
    .pipe(uglify({
      preserveComments: 'license',
      compressor: {
        screw_ie8: true,
      },
      output: {
      },
    }))
    .pipe(gulp.dest('./playlistdc/static/')))
