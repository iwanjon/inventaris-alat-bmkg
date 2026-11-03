// import { defineConfig } from "vite";
// import react from "@vitejs/plugin-react";
// import path from "path";

// export default defineConfig({
//   plugins: [react()],
//   resolve: {
//     alias: {
//       "@": path.resolve(__dirname, "./src"),
//     },
//   },
//   server: {
//     port: 8080,
//     proxy: {
//       "/api": {
//         target: "http://localhost:8001",
//         changeOrigin: true,
//       },
//       "/uploads": {
//         target: "http://localhost:8001",
//         changeOrigin: true,
//       },
//     },
//   },
// });


import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig(({ mode }) => {
  // Load environment variables based on the current mode
  const env = loadEnv(mode, process.cwd(), "");

  // Parse port as integer (defaults to 8080 if undefined or invalid)
  const port = Number(env.VITE_PORT) || 8080;
  const backendUrl = env.VITE_BACKEND_URL || "http://localhost:8001";

  return {
    plugins: [react()],
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
    server: {
      port: port,
      proxy: {
        "/api": {
          target: backendUrl,
          changeOrigin: true,
        },
        "/uploads": {
          target: backendUrl,
          changeOrigin: true,
        },
      },
    },
  };
});