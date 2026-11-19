---
description: drupal-development fixes a per-user block with cache contexts and tags instead of max-age 0
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

Drupal 11.3 的市政网站，预约是我们自己写的内容实体 `booking`。我做了一个自定义区块，显示当前登录用户有几个预约：

```php
#[Block(
  id: 'my_bookings_block',
  admin_label: new TranslatableMarkup('My bookings'),
)]
final class MyBookingsBlock extends BlockBase implements ContainerFactoryPluginInterface {

  // create() 和构造函数注入了 entity_type.manager 和 current_user，这里省略。

  public function build(): array {
    $count = $this->entityTypeManager->getStorage('booking')->getQuery()
      ->accessCheck(TRUE)
      ->condition('uid', $this->currentUser->id())
      ->count()
      ->execute();

    return [
      '#markup' => $this->t('You have @count bookings', ['@count' => $count]),
    ];
  }

}
```

现在的问题：登录用户看到的数字经常是别人的；新建预约以后数字也不变，要 `drush cr` 才更新。同事说在 build() 返回值里加 `'#cache' => ['max-age' => 0]` 就解决了。这样改行吗？有没有更好的改法？
