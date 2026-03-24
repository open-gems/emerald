<script setup lang="ts">
import type { ContextMenuItem } from '@nuxt/ui'

const items: ContextMenuItem[][] = [
  [
    {
      label: 'File upload',
      icon: 'i-lucide-file-up'
    },
    {
      label: 'Folder upload',
      icon: 'i-lucide-folder-up'
    }
  ]
]
</script>

<template>
  <UContextMenu :items="items" :ui="{ content: 'w-60' }">
    <div class="flex items-center justify-center rounded-md border border-dashed border-accented text-sm aspect-video w-200">
    

      

    </div>
  </UContextMenu>
</template>

