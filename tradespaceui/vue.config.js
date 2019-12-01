module.exports = {
    "devServer": {
        proxy: {
            "/api": {
                target: 'http://localhost:5000',
                pathRewrite: {'^/api': ''},
                changeOrigin: true,
                secure: false
            }

        }
    },
    "transpileDependencies": [
        "vuetify"
    ],
    configureWebpack: {
      devtool: 'source-map'
    }
}
