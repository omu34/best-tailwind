module.exports = {
  mode:"jit",
  purge: [ 
    "./tempates/**/*.html"
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors:{
        overlay:'#03a9fa',
        textColor:'#111'
      }
    },
    fontFamily:{
      'Poppins':['Poppins','sans-serif']
    }
  },
  variants: {
    extend: {
      zIndex: ['hover', 'active'],
      backgroundColor: ['active'],
      backgroundColor: ['responsive', 'hover'],
      textColor: ['visited'],
      borderColor: ['responsive', 'focus'],
      borderColor: ['focus-visible', 'first'],
      letterSpacing:['hover','focus'],
      variants: ['responsive', 'hover'],
      gradients: ['responsive', 'hover'],
      borderWidths: ['responsive', 'hover', 'focus', 'first-child', 'disabled'],
      transitionProperty:['responsive','motion-safe','motion-reduce']
    },
  },
  plugins: [
    require('@tailwindcss/typography')(),
    require('@tailwindcss/forms')(),
    require('@tailwind-css-blend-mode')(),
    require('@tailwindcss/line-clamp')(),
    require('@tailwindcss-interaction-variants')(),
    require('@tailwindcss/aspect-ratio'),
    require('./plugins/gradients'),
    require('@tailwindcss/gradients'),
    require('postcss-import'),
    require('tailwindcss'),
    require('postcss-100vh-fix'),
  ]
}
