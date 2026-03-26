<script setup lang="ts">
import type { ContextMenuItem } from "@nuxt/ui";

const documentStore = useDocumentStore();

await documentStore.getFolders();

const contextItems: ContextMenuItem[][] = [
  [
    {
      label: "New folder",
      icon: "i-lucide-folder-plus",
    },
  ],
];

</script>

<template>
  <div class="index-page">
    <UContextMenu disabled :items="contextItems" :ui="{ content: 'w-60' }">
      <HomeFolderGrid />
    </UContextMenu>
  </div>
</template>

<style lang="css" scoped>
.index-page {
  flex-direction: column;
  display: flex;
  height: 100%;
  width: 100%;
}
</style>
