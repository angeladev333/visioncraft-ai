const nextConfig = {
    rewrites: async () => {
      return [
        {
          source: '/api/:path*',
          destination:'http://127.0.0.1:5000/:path*'
        },
      ]
    },
    experimental: {
      proxyTimeout: 100000,
    }
  }
  
  module.exports = nextConfig