import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import fs from 'fs'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 80,
    // https: {
    //   key: fs.readFileSync(path.resolve(__dirname, 'path/to/your/private.pem')),
    //   cert: fs.readFileSync(path.resolve(__dirname, 'path/to/your/file.crt'))
    // }
  }
})