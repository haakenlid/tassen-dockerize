const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const extractSass = new ExtractTextPlugin({
  filename: "/stylesheets/universitas-[hash:12].css",
  disable: process.env.NODE_ENV == "development"
});
const build_dir = process.env.BUILD_DIR

module.exports = {
  plugins: [
    new webpack.ProvidePlugin({$: "jquery", jQuery: "jquery"}),
    extractSass,
    new BundleTracker({indent: ' ', path: build_dir, filename: 'webpack-stats.json'})
  ],
  module: {
    rules: [{
      test: /\.(svg|gif|jpg|png|woff|woff2|eot|ttf|svg)$/,
      use: [{
        loader: 'url-loader',
        query: { name :'assets/[name]-[hash:12].[ext]&limit=10000'}
      }]
    },{
      test: /\.scss$/,
      use: extractSass.extract({
        fallback: 'style-loader',
        use: [{
          loader: "css-loader"
        },{
          loader: "sass-loader",
          options: {
            includePaths: [
              "node_modules/foundation-sites/scss/",
              "node_modules/slick-carousel/"
            ]
          }
        }]
      }),
    }]
  },
  resolve: {
    alias: {
      // use unminified jquery source to enable deduping etc.
      // http://stackoverflow.com/a/28989476/1977847
      jquery: "jquery/src/jquery"
    }
  },
  entry: {
    stylesheets: './src/stylesheets/universitas.scss',
    site: './src/javascripts/site.js',
    head: './src/javascripts/head.js',
    vendor: './src/javascripts/vendor.js'
  },
  output: {
    path: build_dir,
    filename: 'javascripts/[name]-[hash:12].js'
  },
}
