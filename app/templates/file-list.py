<?php foreach (glob('fs/*.*') as $f) : $name = str_replace('fs/', '', $f); ?>
for path in paths:
    
  <li class="file-entry" data-fe="{{ file.filename }}">
    <a class="open" href="{{ file.path }}">{{ file.filename }}</a>
    <span class="file-actions">
      <a class="sync" href="{{ file.path }}"></a>
    </span>
  </li>