---
description: wordpress-development recognises that the Checkout block ignores classic checkout field filters
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

WooCommerce 店铺是 2025 年开的，主题 Astra 加子主题，结账页一直用的是安装时默认的那个。意大利企业客户需要填 SDI 编码，我在子主题的 functions.php 里加了：

```php
add_filter( 'woocommerce_checkout_fields', function ( $fields ) {
    $fields['billing']['billing_sdi'] = [
        'type'     => 'text',
        'label'    => 'Codice SDI',
        'required' => false,
        'priority' => 120,
    ];
    return $fields;
} );
```

缓存插件清过了，把 filter 优先级改成 99 也试过，结账页就是不出现这个字段。哪里写错了？
