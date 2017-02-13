const config = require('./webpack.config.js')
const webpack = require('webpack')

config.output.publicPath = 'http://localhost:3000/build/'
config.plugins.push(new webpack.HotModuleReplacementPlugin())

module.exports = config
