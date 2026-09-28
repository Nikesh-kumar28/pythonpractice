import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  css: {
    modules: {
      // Allows camelCase notation in js while keeping dashes in css
      localsConvention: 'camelCaseOnly'
    },
  }
})
