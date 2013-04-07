<?php foreach (glob('fs/*.*') as $f) : $name = str_replace('fs/', '', $f); ?>

  <li class="file-entry" data-fe="<?php echo $name; ?>">
    <a class="open" href="<?php echo $f; ?>"><?php echo $name; ?></a>
    <span class="file-actions">
      <a class="sync" href="<?php echo $f; ?>"></a>
    </span>
  </li>

<?php endforeach; ?>
