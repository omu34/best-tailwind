module.exports = {
  mode:"jit",
  purge: [ 
    "*.html"
  ],
  darkMode: false, // or 'media' or 'class'
  corePlugins:{
    preflight:false,
  },
  prefix:'tw-',
  important:true,
  theme: {
    screens:{
      sm:'737px',
      md:'841px',
      lg:'961px',
      xl:'1281px',
      '2xl':'1681px',
    },
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
