module.exports = {
  exclude:[
    __dirname+'/knock/**',
    __dirname+'/knockKnock/**',
    __dirname+'/templates/**',
    __dirname+'/**.sqlite3',
    __dirname+'/**.py',
    __dirname+'/**.json',
    __dirname+'/**.js',
  ],
  plugins: [
    "@snowpack/plugin-sass",
    "@snowpack/plugin-postcss"
  ],
  installOptions:{
    treeshake:true
  },
  buildOptions:{
    // baseUrl: "/static/",
    watch: true,
    // out: ".",
    // clean: true
  },
  devOptions: {
    open: 'none',
  },
}
