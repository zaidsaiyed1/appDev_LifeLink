export default ({ config }) => {
              const isDev = process.env.APP_ENV === 'development';
            
              return {
                ...config,
                extra: {
                  API_URL: isDev
                    ? "http://192.168.1.15:8000"
                    : "https://your-production-backend.com"
                }
              };
            };
            