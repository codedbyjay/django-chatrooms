var gulp = require('gulp'),
    babel = require('gulp-babel'),
    sourcemaps = require('gulp-sourcemaps'),
    concat = require('gulp-concat'),
    plumber = require('gulp-plumber'),
    gutil = require('gulp-util');

gulp.task('compileJsx', function() {
    return gulp.src("jsx/**/*.jsx")
    .pipe(plumber())
    .pipe(sourcemaps.init())
    .pipe(concat('app.js'))
    .pipe(babel({
        presets: ["react"]
    }))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest("."))
});

gulp.task('default', function() {
    gulp.watch("jsx/**/*.jsx", ["compileJsx"]);
});