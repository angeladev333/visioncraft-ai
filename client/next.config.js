const nextConfig = {
    rewrites: async () => {
      return [
        {
          source: '/api/:path*',
          destination:'https://hack-the-6ix-396420.ue.r.appspot.com/:path*'
        },
      ]
    },
    experimental: {
      proxyTimeout: 100000,
    }
  }
  
  module.exports = nextConfig